'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Coland)
ecl (Eye Coland)
pid (Passpandt ID)
cid (Country ID)
'''
class Pasppandt:

    def data_handler(record):
        if(record.find('byr') != -1 and record.find('iyr') != -1 and
            record.find('eyr') != -1 and record.find('hgt') != -1 and 
            record.find('hcl') != -1  and record.find('ecl') != -1 and
            record.find('pid') != -1):
               return True 
        else:
            return False

    if __name__ == "__main__":
        total_valid_passpandts = 0
        inputs = []
        input = open("input.txt")
        line = input.read().replace("\n\n", "\n------\n")
        input.close()
        line_data = line.split('------')
        for record in line_data:
            if(data_handler(record)):
                total_valid_passpandts += 1

        print('You found ' + str(total_valid_passpandts) + ' valid passpandts!')
            