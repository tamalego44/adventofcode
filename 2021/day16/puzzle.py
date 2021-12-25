def parseInput():
    if False:
        filename = "sample3.txt"
    else:
        filename = "input.txt"

    with open(filename) as file:
        for line in file:
            data = line.strip()
    
    padlength = len(data) * 4
    data = bin(int(data, 16))[2:]
    # if len(data) % 4 > 0: # Pad with zeroes
    #     data = "0" * (4 - (len(data) % 4)) + data
    data = data.zfill(padlength)
    
    return data

class Packet:
    def __init__(self, data):
        #print(data)

        self.original_data = data
        self.header = data[0:6]
        self.data = data[6:]
        self.packets = []

        self.version = int(self.header[0:3], 2)
        self.type = int(self.header[3:6], 2)

        self.handle()

    def handle(self):
        if(self.type == 4):
            #Literal value
            val = ''
            while self.data[0] != '0':
                val += self.data[1:5]
                self.data = self.data[5:]
            
            val += self.data[1:5]
            self.data = self.data[5:]
            self.value = int(val, 2)
        else:
            length_id = self.data[0]
            self.data = self.data[1:]
            if length_id == '0':
                length = int(self.data[0:15], 2)
                self.data = self.data[15:]
                self.length = length
                packet_data = self.data[0:self.length]
                self.data = self.data[self.length:]

                while length > 0:
                    #print(self.packet_data)
                    #print(len(packet_data))
                    new_packet = Packet(packet_data)
                    length -= len(packet_data) - len(new_packet.data)
                    packet_data = new_packet.data
                    self.packets.append(new_packet)

            else:
                length = int(self.data[0:11], 2)
                self.data = self.data[11:]
                self.length = length

                while length > 0:
                    new_packet = Packet(self.data)
                    length -= 1
                    self.data = new_packet.data
                    self.packets.append(new_packet)
    
    def calculate(self):
        if self.type == 0: # Sum
            val = 0
            for packet in self.packets:
                val += packet.calculate()
        elif self.type == 1: # Product
            val = 1
            for packet in self.packets:
                val *= packet.calculate()
        elif self.type == 2: # Minimum
            vals = [p.calculate() for p in self.packets]
            val = min(vals)
        elif self.type == 3: # Maximum
            vals = [p.calculate() for p in self.packets]
            val = max(vals)
        elif self.type == 4: # Literal
            val = self.value
        elif self.type == 5: # Greater Than
            val = 1 if self.packets[0].calculate() > self.packets[1].calculate() else 0
        elif self.type == 6: # Less Than
            val = 1 if self.packets[0].calculate() < self.packets[1].calculate() else 0
        else: # Equals
            val = 1 if self.packets[0].calculate() == self.packets[1].calculate() else 0
        
        return val

    def __str__(self):
        ret = ""
        ret += "Packet: %s\n" % self.original_data
        ret += "Version: %d\n" % self.version
        ret += "Type: %d\n" % self.type

        if self.type == 4:
            ret += "Value: %d\n" % self.value
        else:
            ret += "Length: %d\n" % self.length
            ret += "Subpackets: %d\n" % len(self.packets)
            ret += "================\n"
            for packet in self.packets:
                ret += packet.__str__() + "\n"
            ret += "================\n"

        return ret


def part1():
    data = parseInput()

    packet = Packet(data)
    
    q = [packet]
    score = 0
    while len(q) > 0:
        p = q.pop(0)
        score += p.version
        q += p.packets

    
    return score


def part2():
    data = parseInput()

    packet = Packet(data)

    return packet.calculate()

print("Part 1 solution:")
print(part1())

print("Part 2 solution:")
print(part2())
