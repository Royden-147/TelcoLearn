import json

file1 = r"C:\Users\ROYDEN\OneDrive\Desktop\phytelco\Day_22\scr1.json"
file2 = r"C:\Users\ROYDEN\OneDrive\Desktop\phytelco\Day_22\scr2.json" 
resfile = r"C:\Users\ROYDEN\OneDrive\Desktop\phytelco\Day_22\res.json"

with open(file1, 'r') as f1, open(file2, 'r') as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

merged = [data1, data2]  

with open(resfile, 'w') as rf:
    json.dump(merged, rf, indent=4)

print("Files have been merged and saved to", resfile)


# fdea6d5646535a4c4686098da93fd929   ipapi - keyy