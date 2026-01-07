from PIL import Image
import os

def convert_images(
    files,
    output_dir,
    target_format,
    quality=90,
    dpi=300,
    progress_callback=None
):
    total = len(files)

    if target_format == "PDF":
        images = []

        for i, file in enumerate(files):
            img = Image.open(file).convert("RGB")
            images.append(img)

            if progress_callback:
                progress_callback(i + 1, total)

        output_path = os.path.join(output_dir, "converted.pdf")
        images[0].save(
            output_path,
            save_all=True,
            append_images=images[1:],
            resolution=dpi
        )
        return total

    for i, file in enumerate(files):
        img = Image.open(file)
        name = os.path.splitext(os.path.basename(file))[0]

        output_path = os.path.join(
            output_dir, f"{name}.{target_format.lower()}"
        )

        if target_format == "JPG":
            img = img.convert("RGB")
            img.save(output_path, "JPEG", quality=quality)

        elif target_format == "PNG":
            img.save(output_path, "PNG")

        elif target_format == "WEBP":
            img.save(output_path, "WEBP", quality=quality)

        if progress_callback:
            progress_callback(i + 1, total)

    return total
