from calendar import different_locale
import hashlib

# get hash file
def getHash(file):
    # make the default file format to sha
    hash = hashlib.sha1()

    #open the file in 1024 bytes(asyn)
    chunk = 0
    with open(file,'rb') as f:
        while chunk != b'':
            chunk = f.read(1024)
            hash.update(chunk)

        #retun in hash format
        return f"{hash.hexdigest()}, {f.name}"

file1 = print(getHash('file1 copy.txt'))

#To find similar hash reports
def compareHash(filesArr, hash):
    similar_reports = []
    different_reports = []

    for file in filesArr:
        file = getHash(file)
        if file == hash:
            similar_reports.append(hash)
        else:
            different_reports.append(file)

    return {
        'similar_reports' : similar_reports,
        'different_reports' : different_reports,
    }    


data = compareHash(['file1.txt', 'file1 copy.txt','file1 copy 2.txt'], getHash('file1.txt'))

# locate similar reports
def findTheFiles():
    similar_report = data['similar_reports']

        




#0123
#0123

            

    


