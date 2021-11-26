#!/usr/bin/env bash

CUDA_VISIBLE_DEVICES=1 PORT=29501 ./tools/dist_train.sh configs/swin/upernet_swin_base_patch4_window7_512x1024_80k_cityscapes_ade20k_pretrain_224x224_22K.py 1