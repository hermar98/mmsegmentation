_base_ = [
    './upernet_swin_tiny_patch4_window7_512x1024_80k_cityscapes_'
    'pretrain_ade_imagenet_224x224_1K.py'
]
model = dict(
    #pretrained='pretrain/swin_base_patch4_window7_224.pth',
    backbone=dict(
        embed_dims=128, depths=[2, 2, 18, 2], num_heads=[4, 8, 16, 32]),
    decode_head=dict(in_channels=[128, 256, 512, 1024], num_classes=30),
    auxiliary_head=dict(in_channels=512, num_classes=30))
