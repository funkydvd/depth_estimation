hf = figure()

x = [300,500,800,1000,1500,2000,3000,5000,7000,10000,20000,30000,1000000]/100
y= [45.34,71.40, 45.35, 49.14,64.18,60.53,57.36,55.20,62.41,62.35,56.22, 48.19,37.89]
plot(x,y)

xlabel("size")
ylabel("RMSE")
hold on

x = [300,500,800,1000,1500,2000,3000,5000,7000,10000,20000,30000,1000000]/100
y = [56.89, 86.14, 72.30, 61.77, 66.65, 74.67, 69.63, 69.78, 84.81, 77.77, 72.73, 60.36, 42.66]
plot(x,y)

x = [300,500,800,1000,1500,2000,3000,5000,7000,10000,20000,30000,1000000]/100
y = [45.66, 71.65, 51.85, 50.12, 59.12, 62.95, 55.21, 55.98, 64.98, 62.38, 57.10, 49.66, 37.15]
plot(x,y)

x = [300,500,800,1000,1500,2000,3000,5000,7000,10000,20000,30000,1000000]/100
y = [52.22, 75.35, 54.91, 55.60, 60.69, 62.69, 62.53, 60.77, 72.65, 68.34, 63.27, 52.18, 38.47]
plot(x,y)

x = [300,500,800,1000,1500,2000,3000,5000,7000,10000,20000,30000,1000000]/100
y = [57.85, 79.00, 73.99, 61.28, 70.20, 79.62, 71.03, 70.29, 83.19, 77.70, 68.08, 59.10, 40.04]
plot(x,y)

x = [300,500,800,1000,1500,2000,3000,5000,7000,10000,20000,30000,1000000]/100
y = [41.52, 60.84, 52.47, 58.32, 38.77, 54.66, 55.70, 64.08, 75.32, 62.74, 72.91, 70.45, 62.02]
plot(x,y)

legend("Megadepth", "DORN", "LKVOLearner", "SfMLearner","Monodepth" ,"DenseDepth")

print (hf, "plot2.pdf");
