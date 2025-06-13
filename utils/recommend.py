def get_recommendation(skin_type):
    recommendations_map = {
        "dry": {
            "type": "Kering",
            "description": "Kulit kering membutuhkan hidrasi ekstra dan perawatan yang melembabkan.",
            "recommendations": [
                "Gunakan pembersih yang tidak mengeringkan",
                "Aplikasikan serum hyaluronic acid",
                "Gunakan moisturizer yang kaya dan menutrisi",
            ],
        },
        "oily": {
            "type": "Berminyak",
            "description": "Kulit berminyak memproduksi sebum berlebihan, terutama di T-zone.",
            "recommendations": [
                "Gunakan pembersih berbahan salisilat acid",
                "Aplikasikan toner untuk mengontrol minyak",
                "Pilih moisturizer oil-free",
            ],
        },
        "normal": {
            "type": "Normal",
            "description": "Kulit normal memiliki keseimbangan minyak dan kelembaban yang baik.",
            "recommendations": [
                "Gunakan pembersih wajah yang lembut",
                "Aplikasikan moisturizer setiap hari",
                "Jangan lupa sunscreen SPF 30+",
            ],
        }
    }
    return recommendations_map.get(skin_type, None)
