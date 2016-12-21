# show stats that who talk most.
# csvcut -c User chat.csv | csvstat

# filter messages spoken by "이름".
csvcut -c User,Message chat.csv | csvgrep -c User -m 이름 | csvcut -c Message | csvlook > jeon.txt
