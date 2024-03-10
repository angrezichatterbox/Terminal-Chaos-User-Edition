echo "Enter code:"
read -r encoded_input

decoded_output=$(echo "$encoded_input" | base64 -d)

echo -e "\n$decoded_output"
