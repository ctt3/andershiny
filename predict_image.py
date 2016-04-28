# Import Block
import pickle,sys

def main(n):
  # predict single image
  image_num = int(n) - 1000
  pixels = pickle.load( open( "pixels.p", "rb" ) )
  forest = pickle.load( open( "forest.p", "rb" ) )

  print forest.predict(pixels[image_num].reshape(1, -1))[0]

if __name__ == "__main__": main(sys.argv[1])