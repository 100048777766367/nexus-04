100048777766367/nexus-04/
├── cells/
│   ├── linguistic_cell.py
│   └── neuron.py
├── adapters/
│   └── universal_adapter.py
├── mechanisms/                      # 🧩 NƠI PHÂN BÀO VÀ PHONG TƯỚC DIỄN RA
│   ├── base.py
│   ├── mitosis.py                   # 🆕 [CƠ CHẾ 1]: Giám sát kích thước & Tự kích hoạt Phân Bào
│   ├── reliquary.py                 # 🆕 [CƠ CHẾ 2]: Nhà Tưởng Niệm, Trao Bằng Khen, Hoa, Huy Chương
│   ├── knowledge_graph.py
│   ├── actuator.py
│   │
│   └── consensus_organ/             # 🏛️ [VÍ DỤ TỆP consensus.py ĐÃ PHÂN BÀO THÀNH THƯ MỤC]
│       ├── .lineage_manifest.json   # Căn cước phả hệ: Mẹ là consensus.py (Thế hệ F1)
│       ├── voter_TheJust.py         # Con trưởng: Được phong Hậu hiệu "TheJust"
│       └── quorum_collector.py      # Con thứ: Chuyên trách gom phiếu đa luồng
│
├── synapses/
│   ├── peers.json
│   ├── state.json
│   ├── ancestral_reliquary.json     # 🕯️ Nhà Tưởng Niệm lưu giữ di cốt các tệp tiền bối
│   └── honors_registry.json         # 🎖️ Bảng vàng Huân Huy Chương, Bằng Khen, Thẻ Bài
│
├── engine.py                        # 🌌 [VI NHÂN F4]: Quét đệ quy os.walk xuyên mọi thư mục con cháu!
├── Dockerfile
└── .github/
    └── workflows/
        └── node.yml
