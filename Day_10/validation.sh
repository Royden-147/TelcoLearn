read -p "Enter Name: " name
read -p "Enter Age: " age

if [[ $name =~ ^[A-Za-z]+$ ]] && (( 0<age && age< 100 )); then		# regex for name and also validation of age
echo "Valid"
else
echo "Invalid"
fi

