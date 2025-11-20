read -p "Do you want to check your System Stats? (Yes/Yes): " req
if [ $req == "Yes" ]; then
echo "The CPU report -- >"  
lscpu
echo "Memory report -- >"
free -h
echo "Disk report -- >"
df -h
else
echo "Byee" 
fi

