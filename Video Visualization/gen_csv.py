import csv

info_list = []

with open("position.txt") as f:
    info_list = f.readline().split("SIMD4<Float>")
    info_list = info_list[1:]
for i in range(len(info_list)):
    info = info_list[i].replace("(","").replace(")","").replace(" ","").split(",")
    info = info[:3]
    for j in range(3):
        info[j] = float(info[j])
    info_list[i] = info

with open("pose.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["X","Y","Z"])
    writer.writerows(info_list)