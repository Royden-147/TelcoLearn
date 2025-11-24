 #!/bin/bash

output="s31_q2_scriptedshells.txt"

{
    echo "Users with non-binary login shells"
    echo "----------------------------------------"

    getent passwd | while IFS=: read -r user _ _ _ _ _ shell; do  # user:password:UID:GID:GECOS:home-dir:shell
        
        [ -z "$shell" ] && continue
        
            if [ -f "$shell" ]; then
            
            real_shell=$(readlink -f "$shell")
            file_output=$(file -b "$real_shell")

            if [[ "$file_output" != *"ELF"* ]]; then
                echo "$user --> $shell"
            fi
        fi
    done
} > "$output"

read -p "Do you want to View all users? " rep
echo -e "\n"
echo "Listing all Users:"
echo -e "\n"
if [ $rep = "yes" ]; then
	awk -F: '$3 >= 1000 {printf "%-15s %-30s %s\n", $1, $6, $7}' /etc/passwd
fi
echo -e "\n"
echo "Updated: $output"