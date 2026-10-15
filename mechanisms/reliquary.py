import os
import json
import time
from mechanisms.base import BaseMechanism

RELIQUARY_FILE = "synapses/ancestral_reliquary.json"
HONORS_FILE = "synapses/honors_registry.json"

class ReliquaryMechanism(BaseMechanism):
    name = "reliquary"
    priority = 45

    def execute(self, context):
        epoch = context.get("current_epoch", 1)
        timestamp = int(time.time())

        # 1. Bàn Thờ Tổ Tiên (Ancestral Reliquary)
        reliquary = {"altar_of_ancestors": []}
        if os.path.exists(RELIQUARY_FILE):
            try:
                with open(RELIQUARY_FILE, "r", encoding="utf-8") as f: reliquary = json.load(f)
            except Exception: pass

        retiree = context.get("memorial_retiree")
        if retiree:
            memorial_record = {
                "consecrated_at_epoch": epoch,
                "timestamp": timestamp,
                "entity": retiree["name"],
                "epitaph": retiree["merit"],
                "offerings": ["Fresh_White_Lotus", "Eternal_Flame", "Golden_Certificate"]
            }
            reliquary["altar_of_ancestors"].append(memorial_record)
            print(f"🕯️ [NHÀ TƯỞNG NIỆM] Đã cúng dường Hoa Sen trắng và khắc bia tưởng niệm: {retiree['name']}")

        # 2. Bảng Vàng Huân Chương (Honors Registry)
        honors = {"hall_of_fame": []}
        if os.path.exists(HONORS_FILE):
            try:
                with open(HONORS_FILE, "r", encoding="utf-8") as f: honors = json.load(f)
            except Exception: pass

        decision = context.get("final_decision", 0.5)
        if abs(decision - 0.5) > 0.35:
            award = {
                "epoch": epoch,
                "badge": "Medal_of_Absolute_Clarity",
                "recipient": "Swarm_Council",
                "passport": "VIP_Consensus_Ticket_F4",
                "tribute": "Golden_Lotus_Laurel"
            }
            honors["hall_of_fame"].append(award)
            print("🎖️ [TRAO HUÂN CHƯƠNG] Bầy nơ-ron nhận 'Huy Chương Đại Giác Ngộ F4'!")

        os.makedirs("synapses", exist_ok=True)
        with open(RELIQUARY_FILE, "w", encoding="utf-8") as f:
            json.dump(reliquary, f, indent=4, ensure_ascii=False)
        with open(HONORS_FILE, "w", encoding="utf-8") as f:
            json.dump(honors, f, indent=4, ensure_ascii=False)
