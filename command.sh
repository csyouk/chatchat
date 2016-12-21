# show stats that who talk most.
# csvcut -c User chat.csv | csvstat

# filter messages spoken by "이름".
echo "Type the name u want to analyze : "
read name
csvcut -c User,Message chat.csv | csvgrep -c User -m $name | csvcut -c Message | csvlook > $name.txt
