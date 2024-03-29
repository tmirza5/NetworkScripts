
#   Copyright 2024 Muhammad Taqi Mirza
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

import pythonping
from pythonping import ping

ip_start = int(input("What is the starting IP address? (input the portion after the last d.p)\n"))
ip_end = int(input("What is the ending IP address? (input the portion after the last d.p)\n"))
subnet = input("What is the subnet? (Enter the numbers before the last d.p (include the d.ps))\n")

for num in range(ip_start, ip_end):
    ping(f"{subnet}.{num}", verbose=True)
    
