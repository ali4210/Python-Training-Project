# Write manually with proper CSV formatting
with open('mycsvfile.csv', 'w') as file:
    file.write("Filesystem,Size,Used,Avail,Use%,Mounted,Date,IP,Role\n")
    file.write("udev,7.8G,0,7.8G,0,/dev,2025-11-01 02:33:12,192.168.0.150,master\n")
    file.write("/dev/sda1,79G,37G,38G,50,/,2025-11-01 02:33:12,192.168.0.150,master\n")