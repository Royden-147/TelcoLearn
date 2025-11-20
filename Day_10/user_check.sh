if [ $UID -eq 0 ]; then
echo "Root User"
else
echo "Normal User"
fi

read -p "NUM 1:" num1
read -p "NUM 2:" num2
if [ $num1 -ge $num2 ];then 
echo "Yes"
else
echo "No"
fi
