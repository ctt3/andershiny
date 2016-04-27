# Import Block
from PIL import Image
import os

# Define Constants

CONFIG = {
  'data'    : "./CIFAR-10/",
  'n_pics'  : 5000,
  'targets' : "./CIFAR-10/trainLabels.csv",
  'train'   : {
    'directory' : "./CIFAR-10/train/",
    'pic_list'  : os.listdir("./CIFAR-10/train/"),
    'file'      : "./CIFAR-10/train_raw.csv"
  },
  'test'    : {
    'directory' : "./CIFAR-10/test/",
    'pic_list'  : os.listdir("./CIFAR-10/test/"),
    'file'      : "./CIFAR-10/test_raw.csv"
  }
}

def get_targets():
  # Get Target Labels
  labels = []
  with open(CONFIG['targets'], 'r') as label_file:
    for line in label_file:
      label = line.rstrip().split(',')[1]
      labels.append(label)

  return labels

def write_headers(outfile, data_type):
  # write pixel headers to file
  arr = []
  for i in range(0,32*32):
    for j in ['r','g','b']:
      arr.append('"px' + j + str(i) + '"')
  if data_type == "train": arr.append('"class"')

  outfile.write(",".join(arr)+'\n')

def main(data_type="train"):
  #reference: 
  #https://github.com/christopher-beckham/kaggle-cifar10-extract/blob/master/getpx.py 
  DATA = CONFIG[data_type]
  if data_type == "train": targets = get_targets()
  with open(DATA['file'], "w") as raw:
    write_headers(raw, data_type)

    # Write pixels to file from images
    for x in range(CONFIG['n_pics']):
      pic_dir = DATA['directory'] + DATA['pic_list'][x]
      im = Image.open(pic_dir)
      arr = []
      for i in range(0, 32):
          for j in range(0, 32):
            tp = im.getpixel((i,j))
            arr.append( str(tp[0]) ) # R
            arr.append( str(tp[1]) ) # G
            arr.append( str(tp[2]) ) # B

      if data_type == "train":
        pic_string = ",".join(arr) + "," + targets[x]+'\n'
      elif data_type == "test":
        pic_string = ",".join(arr) + '\n'

      raw.write(pic_string)

if __name__ == "__main__": main()