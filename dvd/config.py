import os

# ------------------ video download and segmentation configuration ------------------ #
VIDEO_DATABASE_FOLDER = "./video_database/"
VIDEO_RESOLUTION = "360"  # denotes the height of the video
VIDEO_FPS = 2  # frames per second
CLIP_SECS = 10  # seconds

# ------------------ model configuration ------------------ #
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_PROFILE = os.getenv("AWS_PROFILE", None)

AOAI_CAPTION_VLM_MODEL_NAME = "us.anthropic.claude-sonnet-4-20250514-v1:0"

AOAI_ORCHESTRATOR_LLM_MODEL_NAME = "us.anthropic.claude-sonnet-4-20250514-v1:0"

AOAI_TOOL_VLM_MODEL_NAME = "us.anthropic.claude-sonnet-4-20250514-v1:0"
AOAI_TOOL_VLM_MAX_FRAME_NUM = 50

AOAI_EMBEDDING_LARGE_MODEL_NAME = "cohere.embed-multilingual-v3"

# ------------------ agent and tool setting ------------------ #
LITE_MODE = (
    True  # if True, only leverage srt subtitle, no pixel downloaded or pixel captioning
)
GLOBAL_BROWSE_TOPK = 300
OVERWRITE_CLIP_SEARCH_TOPK = 0  # 0 means no overwrite and let agent decide

SINGLE_CHOICE_QA = True  # Design for benchmark test. If True, the agent will only return options for single-choice questions.
MAX_ITERATIONS = 3  # Maximum number of iterations for the agent to run
