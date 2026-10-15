import os
import sys
import json
import importlib
import inspect
from mechanisms.base import BaseMechanism

class Nexus04FractalKernel:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/nexus-04")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")
        self.ancestor = f"{self.owner}/nexus-03"
        
        self.context = {
            "repo_name": self.repo_name,
            "owner": self.owner,
            "ancestor": self.ancestor,
            "peers": self.load_initial_peers(),
            "current_epoch": self.load_current_epoch()
        }

    def load_initial_peers(self):
        peers_file = "synapses/peers.json"
        if os.path.exists(peers_file):
            try:
                with open(peers_file, "r") as f: return json.load(f).get("trusted_peers", [])
            except Exception: pass
        return [
            f"{self.owner}/nexus-03", f"{self.owner}/nexus-02", f"{self.owner}/nexus-01", 
            f"{self.owner}/nexus", f"{self.owner}/genome", f"{self.owner}/retina", f"{self.owner}/motor"
        ]

    def load_current_epoch(self):
        state_file = "synapses/state.json"
        if os.path.exists(state_file):
            try:
                with open(state_file, "r") as f: return json.load(f).get("generation_epoch", 0) + 1
            except Exception: pass
        return 1

    # QUÉT ĐỆ QUY os.walk: NẠP TẤT CẢ CÁC TỆP CON CHÁU TRONG CÁC THƯ MỤC CƠ QUAN
    def discover_fractal_mechanisms(self):
        mechanisms = []
        base_mech_dir = os.path.join(os.path.dirname(__file__), "mechanisms")
        sys.path.append(os.path.dirname(__file__))

        for root, dirs, files in os.walk(base_mech_dir):
            for file in sorted(files):
                if file.endswith(".py") and not file.startswith("__") and file != "base.py":
                    rel_dir = os.path.relpath(root, os.path.dirname(__file__))
                    module_name = f"{rel_dir.replace(os.path.sep, '.')}.{file[:-3]}"
                    try:
                        mod = importlib.import_module(module_name)
                        importlib.reload(mod)
                        for _, obj in inspect.getmembers(mod, inspect.isclass):
                            if issubclass(obj, BaseMechanism) and obj is not BaseMechanism:
                                mechanisms.append(obj())
                                print(f"🔌 [VI NHÂN F4 NẠP ĐỆ QUY]: '{obj.name}' từ '{rel_dir}/{file}'")
                    except Exception as e:
                        print(f"⚠️ [LỖI NẠP {file}]: {e}")

        mechanisms.sort(key=lambda m: getattr(m, 'priority', 100))
        return mechanisms

    def run(self):
        print("=" * 70)
        print(f"🏵️ [NEXUS-04 FRACTAL KERNEL] KHỞI ĐỘNG THẾ HỆ #{self.context['current_epoch']}")
        print(f"👑 Bậc: F4 Siêu Thực Thể Phân Bào Đệ Quy & Nhà Tưởng Niệm Phả Hệ")
        print("=" * 70)

        mechanisms = self.discover_fractal_mechanisms()
        for mech in mechanisms:
            try:
                mech.execute(self.context)
            except Exception as e:
                print(f"🚨 [CÔ LẬP LỖI '{mech.name}']: {e} (Hệ thống tiếp tục tiến hóa)")

        print("=" * 70)
        print(f"✨ [HOÀN TẤT VÒNG ĐỜI F4] Toàn bộ dòng họ tệp & thư mục đã được tri ân!")
        print("=" * 70)

if __name__ == "__main__":
    node = Nexus04FractalKernel()
    node.run()
