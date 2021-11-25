# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)
time_seconds = 30 + (30*60)
time_hours = time_seconds/(60*60)
distance_miles = 10
distance_kilometers = 1.6*distance_miles
speed_kmh = distance_kilometers/time_hours
print(speed_kmh)