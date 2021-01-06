import os

set1 = {}
set2 = {}

for x in range(len(set1)):
	for i in range(8):
		set1[x].append([])



for root, dirs, files in os.walk('rezs_set1'):
	for x in range(len(dirs)): #day, dusk night
		name = root + "/" + dirs[x]; 
		tip = dirs[x][4:]
		map1= {}
		for r2, d2, f2 in os.walk(name):
			for x2 in range(len(d2)): #res x, res y  
				name2 = name + "/" + d2[x2]
				for r3,d3,f3 in os.walk(name2):
					no = r3[-2:]
					if  not(no[0]>='0' and no[0]<='9'):
						no = r3[-1:]
					no = int(no)
					for x3 in range(len(d3)): # mono, mega, etc
						name3 = name2 + "/" + d3[x3]
						category = d3[x3]
						mapa = {}
						for r4,d4,f4 in os.walk(name3):
							fisierele = {}
							for fis in f4:							
								cod = fis[5:]
								cod = cod.split(".")[0]
								cod = cod.split("_")[0]
								
								name4 = name3 + "/" + fis
								fisierele[cod] = name4
							mapa[no] = fisierele
							
							break
						if (category in map1):
							map1[category].update(mapa)
						else:
							map1[category] = mapa
					break
			break
		set1[tip] = map1
					
	break	



for root, dirs, files in os.walk('annotations_set1'):
	for x in range(len(dirs)):
		category = dirs[x]
		map1 = {}
		name = root + "/" + dirs[x];
		for r2, d2, f2 in os.walk(name):
			for fis in f2:
				nr = fis[:-4]
				nr = int(nr)
				name2 = name + "/" + fis
				map1[nr] = name2		
			break
		set1[category]['Annotations'] = map1		
		
	break



for root, dirs, files in os.walk('rezs_set2'):
	for x in range(len(dirs)):
		category = dirs[x][5:]
		name = root + "/" + dirs[x]
		for r2, d2, f2 in os.walk(name):
			for x2 in range(len(d2)):
				name2 = name + "/" + d2[x2]
				tip  = d2[x2]
				mapx = {}
				for r3, d3, f3 in os.walk(name2):
					for x3 in range(len(d3)):
						name3 = name2 + "/" + d3[x3]
						nrl = int(d3[x3])
						for r4,d4,f4 in os.walk(name3):
							fisierele = {}
							for fis in f4:
								
								nr = fis.split("-")[0]
								nr = int(nr)
								fff = name3 + "/" + fis
								fisierele[nr] = fff
							mapx[nrl] = fisierele
							break
						
					break	
				if tip in set2:
					if category in set2[tip]:
						set2[tip][category].update(mapx)
					else:
						set2[tip][category] = mapx
				else:
					set2[tip] = {}
					set2[tip][category] = mapx		
			break
			
	break
	
for root, dirs, files in os.walk('annotations_set2'):
	for x in range(len(dirs)):
		category = dirs[x]
		map1 = {}
		name = root + "/" + dirs[x];
		for r2, d2, f2 in os.walk(name):
			for fis in f2:
				nr = fis[:-4]
				nr = int(nr)
				name2 = name + "/" + fis
				map1[nr] = name2		
			break
		set2[category]['Annotations'] = map1		
		
	break


#for keys in set2['night']:
#	print(keys)
#	print (set2['night'][keys])
#print (set2['night']['Megadepth'])
#print (set1['night']['Megadepth'])

import cv2

classes = []
vals = [0,100,150,200,250,300,400,500,600,700,800,900,1000,1300,1600,2000,3000,4000,5000,7000,10000,20000,30000,1000000]
for i in range(len(vals)-1):
	classes.append([vals[i],vals[i+1]])
print(classes)

import math 
import xml.etree.ElementTree as ET
gt = "Megadepth"
for key in set1:
	for key2 in set1[key]:
		if not (key2 == "color" or key2 == "depth" or key2 == "Annotations" or key2 == gt):
#		if (key2 == "color"):
			mse = 0.0
			nrimg = 0
			for key3 in set1[key][key2]:
				imaginile = []
				path = []
				for img in set1[key][key2][key3]:
					nrimg = nrimg + 1
					img1 = cv2.imread(set1[key][key2][key3][img])
					img2 = cv2.imread(set1[key][gt][key3][img])
					img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
					img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
					img1 = cv2.resize(img1,(640,480),interpolation=cv2.INTER_AREA)
					img2 = cv2.resize(img2,(640,480),interpolation=cv2.INTER_AREA)
					#annfis = set2[key]["Annotations"][key3]

					#for ind1 in range(img1.shape[0]):
					#	for ind2 in range(img2.shape[1]):
					#		i1 = float(img2[ind1][ind2])
					#		i2 = float(img1[ind1][ind2])
					#		diff = (i1-i2)*(i1-i2)
					#		mse = mse+(diff/(640*480))
							
					#print(mse)	
			mse = mse/ (nrimg)
			print(nrimg)
			mse = math.sqrt(mse)
			print(key)
			print(key2)
			print(mse)
						
								
# mse raportat la depth, best 2 classifiers for set1 and set2
# idem mse pentru masini, raport total pt day/dusk/night in functie de dimensiune
# grafic cu timpii
