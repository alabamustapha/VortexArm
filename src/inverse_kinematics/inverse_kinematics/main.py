from dora import Node
import pyarrow as pa
import simulator


def main():
    node = Node()
    simulator.run_simulator()
    for event in node:
        if event["type"] == "INPUT":
            if event["id"] == "TICK":
                print(
                    f"""Node received:
                id: {event["id"]},
                value: {event["value"]},
                metadata: {event["metadata"]}"""
                )

            elif event["id"] == "my_input_id":
                # Warning: Make sure to add my_output_id and my_input_id within the dataflow.
                node.send_output(
                    output_id="my_output_id", data=pa.array([1, 2, 3]), metadata={}
                )


if __name__ == "__main__":
    main()
