import os
import argparse
import imageio
from pygifsicle import optimize


parser = argparse.ArgumentParser()
parser.add_argument('indir', type=str, help='Input dir with frames .png')
args = parser.parse_args()

filenames = [os.path.join(args.indir, f) for f in os.listdir(args.indir)]
gif_path = os.path.join(args.indir, "anim.gif")
images = []

with imageio.get_writer(gif_path, mode='I', fps=30) as writer:
    for filename in filenames:
        if filename.endswith(".png"):
            writer.append_data(imageio.imread(filename))
            os.remove(filename)

optimize(gif_path)
print("success:", gif_path)
