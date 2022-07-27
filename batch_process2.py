import os
import time

for jj in range(1,105):
    str0 = "python generate.py.py --outdir=out/projector-latents" + str(jj) + " --dlatents=out/projector" + str(jj) + "/dlatents.npz --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada/pretrained/ffhq.pkl"
    os.system(str0)
