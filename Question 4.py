from typing import Generator


def chunked_file_reader(
    file_path: str, chunk_size_bytes: int = 1024 * 1024
) -> Generator[str, None, None]:
    """Reads a text file lazily in binary chunks, preventing line tearing

    and yielding complete, unbroken lines with minimal memory usage.
    """
    buffer = ""

    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
        while True:
            chunk = file.read(chunk_size_bytes)
            if not chunk:
                # End of file reached; yield any remaining buffered text
                if buffer:
                    yield buffer
                break

            buffer += chunk
            lines = buffer.split("\n")

            # Keep the last partial segment in the buffer for the next chunk
            buffer = lines.pop()

            for line in lines:
                yield line


# --- Usage Example ---
if __name__ == "__main__":
    # Example stream reading 1MB chunks from a large CSV
    csv_file = "large_dataset.csv"

    # Process line-by-line without high memory consumption
    # for line in chunked_file_reader(csv_file, chunk_size_bytes=1024 * 1024):
    #     process_data(line)
    pass