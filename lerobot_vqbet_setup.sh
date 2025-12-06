#!/bin/bash
# ===========================================
# LeRobot Setup and VQ-BeT Evaluation Script
# ===========================================

# Step 1: Create and activate conda environment
echo "Creating conda environment..."
conda create -y -n lerobot python=3.10
conda activate lerobot

# Step 2: Install ffmpeg
echo "Installing ffmpeg..."
conda install ffmpeg -c conda-forge -y

# Step 3: Clone LeRobot repository
echo "Cloning LeRobot repository..."
git clone https://github.com/huggingface/lerobot.git
cd lerobot

# Step 4: Install LeRobot with PushT environment (required for VQ-BeT evaluation)
echo "Installing LeRobot with PushT environment..."
pip install -e ".[pusht]"

# Step 5: Run VQ-BeT evaluation on PushT environment
# Option A: Using the command line evaluation script
echo "Running VQ-BeT evaluation..."
python lerobot/scripts/eval.py \
    --policy.path=lerobot/vqbet_pusht \
    --output_dir=outputs/eval/vqbet_pusht \
    --env.type=pusht \
    --seed=100000 \
    --eval.n_episodes=10 \
    --eval.batch_size=10 \
    --device=cuda

echo "Evaluation complete! Check outputs/eval/vqbet_pusht for results."
