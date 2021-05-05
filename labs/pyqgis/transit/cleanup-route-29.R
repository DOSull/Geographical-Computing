setwd("~/Documents/teaching/GISC-420/labs/scratch/pyqgis/transit")

library(sf)
r29s <- st_read("route-29-stops.gpkg")
r29gtfs <- read.csv("route-29-at-night.csv")
r29sn <- inner_join(r29s, r29gtfs)

r29 <- st_read("route-29.gpkg") %>%
  slice(3)

library(tmap)
tmap_mode("view")
tm_shape(r29sn) + 
  tm_dots() +
  tm_shape(r29) + 
  tm_lines()

library(lubridate)
library(hms)

r29sn <- r29sn %>% arrange(stop_sequence)
r29sn$arrival_time <- as_hms(as_datetime(r29sn$arrival_time, format = "%H:%M:%S"))
r29sn$elapsed_secs <- c(0, cumsum(as.integer(diff(r29sn$arrival_time))))
r29sn$travel_time <- round(r29sn$elapsed_secs / 60, 2)
r29sn <- select(r29sn, 8, 4, 1, 6, 16)

r29sn <- st_transform(r29sn, 2193)
st_write(r29sn, "route-29-stops-at-night-times.gpkg", delete_dsn = TRUE)
