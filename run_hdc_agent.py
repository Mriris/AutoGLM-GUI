"""Run PhoneAgent with HDC device type.

Usage:
    python run_hdc_agent.py "打开设置"
    python run_hdc_agent.py --device-id 192.168.1.100:5555 "打开微信"
    python run_hdc_agent.py --base-url http://localhost:8080/v1 --api-key EMPTY "Open Settings"
"""

import argparse
import sys
import io

from phone_agent.device_factory import set_device_type, DeviceType
from phone_agent import PhoneAgent
from phone_agent.model import ModelConfig
from phone_agent.agent import AgentConfig


def main():
    """Main entry point."""
    # Set UTF-8 encoding for Windows
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Run PhoneAgent with HDC device type",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_hdc_agent.py "打开设置"
  python run_hdc_agent.py --device-id 192.168.1.100:5555 "打开微信"
  python run_hdc_agent.py --lang en "Open Settings"
        """,
    )

    parser.add_argument(
        "task",
        help="Task to execute (e.g., '打开设置', 'Open Settings')",
    )

    parser.add_argument(
        "--device-type",
        choices=["adb", "hdc"],
        default="hdc",
        help="Device type: adb (Android) or hdc (HarmonyOS) (default: hdc)",
    )

    parser.add_argument(
        "--device-id",
        default="127.0.0.1:5555",
        help="Device ID (default: 127.0.0.1:5555)",
    )

    parser.add_argument(
        "--base-url",
        default="https://api-inference.modelscope.cn/v1",
        help="Model API base URL (default: ModelScope API)",
    )

    parser.add_argument(
        "--model",
        default="ZhipuAI/AutoGLM-Phone-9B",
        help="Model name (default: ZhipuAI/AutoGLM-Phone-9B)",
    )

    parser.add_argument(
        "--api-key",
        default="",
        help="API key for the model API",
    )

    parser.add_argument(
        "--lang",
        choices=["cn", "en"],
        default="cn",
        help="Language: cn (Chinese) or en (English) (default: cn)",
    )

    parser.add_argument(
        "--max-steps",
        type=int,
        default=100,
        help="Maximum number of steps (default: 100)",
    )

    args = parser.parse_args()

    # Set device type
    device_type = DeviceType.HDC if args.device_type == "hdc" else DeviceType.ADB
    set_device_type(device_type)

    # Configure model
    model_config = ModelConfig(
        base_url=args.base_url,
        model_name=args.model,
        api_key=args.api_key,
    )

    # Configure agent
    agent_config = AgentConfig(
        device_id=args.device_id,
        lang=args.lang,
        max_steps=args.max_steps,
        verbose=True,
    )

    # Display configuration
    print()
    print("=" * 50)
    print("  PhoneAgent Runner")
    print("=" * 50)
    print(f"  Device Type: {args.device_type.upper()}")
    print(f"  Device ID:   {args.device_id}")
    print(f"  Model:       {args.model}")
    print(f"  Language:    {args.lang}")
    print(f"  Task:        {args.task}")
    print("=" * 50)
    print()

    # Create and run agent
    try:
        agent = PhoneAgent(model_config, agent_config)
        result = agent.run(args.task)
        print()
        print("=" * 50)
        print(f"✅ Final Result: {result}")
        print("=" * 50)
        print()
    except KeyboardInterrupt:
        print()
        print("=" * 50)
        print("⚠️  Task interrupted by user")
        print("=" * 50)
        print()
        sys.exit(1)
    except Exception as e:
        print()
        print("=" * 50)
        print(f"❌ Error: {e}")
        print("=" * 50)
        print()
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
