import uuid, os
#
#  This is a very early prototype, trying to flesh out some ideas as code
#
#  I'm not very versed in python, github, and distributed development, but I'm willing to learn.
#
#  Mike Warot - December 8, 2012
#
id = uuid.uuid4()
path = "c:\\InterTubes_Git\\Top100"

def get_custom_checksum(input_file_name):
    from datetime import datetime
    starttime = datetime.now()
	# START: Actual checksum calculation
    from hashlib import md5, sha1, sha224, sha384, sha256, sha512
    #chunk_size = 1 # 1 byte -- NOT RECOMENDED -- USE AT LEAST 1KB. When 1KB takes 1 min to run, 1B takes 19 minutes to run
    #chunk_size = 1024 # 1 KB
    chunk_size = 1048576 # 1024 B * 1024 B = 1048576 B = 1 MB
    file_sha256_checksum = sha256()
    try:
        with open(input_file_name, "rb") as f:
            byte = f.read(chunk_size)
            previous_byte = byte
            byte_size = len(byte)
            file_read_iterations = 1
            while byte:
                file_sha256_checksum.update(byte)
                previous_byte = byte
                byte = f.read(chunk_size)
                byte_size += len(byte)
                file_read_iterations += 1
    except IOError:
        print ('File could not be opened: %s' % (input_file_name))
        #exit()
        return
    except:
        raise
	# END: Actual checksum calculation
    # For storage purposes, 1024 bytes = 1 kilobyte
    # For data transfer purposes, 1000 bits = 1 kilobit
    stoptime = datetime.now()
    processtime = stoptime-starttime
    custom_checksum_profile = {
        'starttime': starttime,
        'byte_size': byte_size,
        'sha256_checksum': file_sha256_checksum.hexdigest(),
        'stoptime': stoptime,
        'processtime': processtime,
        }
    return custom_checksum_profile


for (path, dirs, files) in os.walk(path):
  print path,"contains"
  for name in files:
      filename = os.path.join(path,name)
      sums = get_custom_checksum(filename)
      print name + "," +  sums['sha256_checksum'] + "," + str(sums['byte_size'])
      

    
