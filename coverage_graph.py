def generate_graph_data(data):

    labels = []
    values = []

    for api in data:
        labels.append(api["endpoint"])
        values.append(api["hit_count"])

    return {
        "labels": labels,
        "values": values
    }