---
title: Fine-tune SmolVLA for an SO-101 pick-and-place task

description: Record SO-101 demonstrations, fine-tune SmolVLA on an Arm-based NVIDIA DGX Spark, and evaluate the model with LeRobot.

minutes_to_complete: 1920

who_is_this_for: This is an advanced topic for robotics and AI developers who want to train a vision-language-action model from their own SO-101 demonstrations.

learning_objectives:
    - Set up a LeRobot environment for SO-101 data collection and SmolVLA training.
    - Connect, calibrate, and teleoperate an SO-101 leader-follower pair with cameras.
    - Record and inspect a pick-and-place dataset, then optionally upload it.
    - Fine-tune and physically evaluate a SmolVLA model on an NVIDIA DGX Spark.

prerequisites:
    - An NVIDIA DGX Spark with at least 30 GB of free storage.
    - An assembled SO-101 leader and follower, two USB cameras, and an unobstructed workspace.
    - A vial or similar graspable object and a stable rack for the placement target.
    - A [Hugging Face account](https://huggingface.co/join) if you want to upload the dataset.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-24T21:06:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 65c3af0b795ae8b91a2aabe35897cb51472bc4ba0162dbe2311a2f5f247fefd0
  summary_generated_at: '2026-08-24T21:06:39Z'
  summary_source_hash: 65c3af0b795ae8b91a2aabe35897cb51472bc4ba0162dbe2311a2f5f247fefd0
  faq_generated_at: '2026-08-24T21:06:39Z'
  faq_source_hash: 65c3af0b795ae8b91a2aabe35897cb51472bc4ba0162dbe2311a2f5f247fefd0
  summary: >-
    You'll collect SO-101 pick-and-place demonstrations, fine-tune SmolVLA with LeRobot, and
    evaluate the resulting policy on an Arm-based NVIDIA DGX Spark. First, you'll set up Python,
    identify the USB devices, calibrate the leader-follower pair, and verify teleoperation. Next,
    you'll record and review multi-camera episodes, optionally upload the dataset, fine-tune the
    model, then assess its control of the physical pick-and-place task.
  faqs:
  - question: How do I know the robot and cameras are mapped to the right devices before calibration?
    answer: >-
      Set `ROBOT_PORT`, `LEADER_PORT`, `GRIPPER_CAMERA_ID`, and `WORKSPACE_CAMERA_ID` in the
      terminal you will use for calibration. If you reconnect a USB device or open a new terminal,
      repeat device discovery and export the current paths before proceeding.
  - question: Which components do I connect where when wiring the setup?
    answer: >-
      Connect the SO-101 leader, SO-101 follower, gripper camera, and workspace camera to the
      DGX Spark over USB. Mount the gripper camera on the follower, and keep the workspace camera
      fixed to frame the follower, pickup area, rack, and the arm’s full range of motion.
  - question: What should I check during calibration so teleoperation mirrors the leader correctly?
    answer: >-
      Start each arm with its joints near the middle of their usable ranges. Move each requested
      joint slowly through its safe range, support the arm, and stop before reaching limits.
  - question: When is the workspace ready to start recording demonstrations?
    answer: >-
      After calibrating and verifying teleoperation, arrange the two-camera workspace. Lay the
      vial on the black mat, place the rack beside it within the follower’s calibrated reach,
      and leave enough space between them for grasping and movement.
  - question: What result should I expect after fine-tuning SmolVLA with my demonstrations?
    answer: >-
      You get a SmolVLA model adapted to your demonstrations. Evaluate it with LeRobot on the
      Arm-based NVIDIA DGX Spark, then use it to control the robot on the vial-to-rack pick-and-place
      task under the recorded conditions.
# END generated_summary_faq

author: Koki Mitsunami

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-X
    - Cortex-A
tools_software_languages:
    - Python
    - PyTorch
    - LeRobot
    - SmolVLA
    - Hugging Face
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: LeRobot installation documentation
        link: https://huggingface.co/docs/lerobot/installation
        type: documentation
    - resource:
        title: LeRobot SO-101 documentation
        link: https://huggingface.co/docs/lerobot/so101
        type: documentation
    - resource:
        title: SmolVLA documentation
        link: https://huggingface.co/docs/lerobot/smolvla
        type: documentation
    - resource:
        title: SmolVLA base model card
        link: https://huggingface.co/lerobot/smolvla_base
        type: documentation
    - resource:
        title: SmolVLA research paper
        link: https://arxiv.org/abs/2506.01844
        type: website
    - resource:
        title: Train an SO-101 Robot From Sim-to-Real With NVIDIA Isaac
        link: https://docs.nvidia.com/learning/physical-ai/sim-to-real-so-101/latest/index.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
