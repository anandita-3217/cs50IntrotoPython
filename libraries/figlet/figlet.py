import sys
import random
import pyfiglet
def main():
  if len(sys.argv) != 1 and len(sys.argv) !=3:
    sys.exit("Invalid usage")
  font = None
  if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f" ,"--font"]:
      sys.exit("Invlid usage")
    font = sys.argv[2]
    if font not in pyfiglet.FigletFont.getFonts():
      sys.exit("Invalid usage")
  text = input("Input: ")  
  if font:
    figlet = pyfiglet.Figlet(font = font)
  else:
    figlet = pyfiglet.Figlet()
  print("Output: \n",figlet.renderText(text))
    

main()
