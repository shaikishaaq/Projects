#!/usr/bin/env python3
"""
LeRobot VQ-BeT Evaluation Script
This script evaluates the pretrained VQ-BeT model on the PushT environment.
"""

from pathlib import Path
import torch

# Import VQ-BeT policy from LeRobot
from lerobot.common.policies.vqbet.modeling_vqbet import VQBeTPolicy

# Set output directory
output_directory = Path("outputs/eval/vqbet_pusht")
output_directory.mkdir(parents=True, exist_ok=True)

# Load pretrained VQ-BeT model from Hugging Face Hub
pretrained_policy_path = "lerobot/vqbet_pusht"
print(f"Loading VQ-BeT policy from {pretrained_policy_path}...")
policy = VQBeTPolicy.from_pretrained(pretrained_policy_path)

# Set device (use CUDA if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
policy.to(device)
policy.eval()

print(f"Model loaded successfully on {device}")
print(f"Model parameters: {sum(p.numel() for p in policy.parameters()):,}")

# Run evaluation using LeRobot's evaluation utilities
from lerobot.scripts.eval import main as eval_main
import argparse

# Configure evaluation arguments
eval_args = argparse.Namespace(
    policy=argparse.Namespace(path=pretrained_policy_path),
    output_dir=str(output_directory),
    env=argparse.Namespace(type="pusht"),
    seed=100000,
    eval=argparse.Namespace(n_episodes=10, batch_size=10),
    device=str(device),
    use_amp=False
)

print("Starting evaluation...")
print("This will run the VQ-BeT model in the PushT simulation environment.")
print("Results will be saved to:", output_directory)
