import os
import re
import click

# Counts the number of episodes (files) in the given folder to determine how many digits the episode number will have to be
def get_episode_digit_count(folder):
    episode_count = 0
    for filename in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, filename)):
            episode_count += 1
    return 2 if episode_count <= 99 else 3


@click.command()
@click.option('--folder', '-f', help='Path to the folder containing TV series episodes.')
@click.option('--show', '-s', help='Name of the TV show.')
@click.option('--remove-after', '-r', help='String after which to remove content from filenames.')
def rename_tv_series(folder, show, remove_after):
    if not folder or not show:
        click.echo('Please provide both --folder and --show options.')
        return

    os.chdir(folder)
    episode_digit_count = get_episode_digit_count(folder)
    pattern = re.compile(r"(\d+)x(\d+)\s+(.*?)\.")

    for filename in os.listdir("."):
        if os.path.isfile(filename):
            # Use os.path.splitext() to extract the base name and extension
            base_name, file_extension = os.path.splitext(filename)

            match = pattern.search(base_name)
            if match:
                season = match.group(1).zfill(2)
                episode = match.group(2).zfill(episode_digit_count)
                episode_name = match.group(3)

                # Remove content after the specified string
                if remove_after and remove_after in episode_name:
                    episode_name = episode_name.split(remove_after, 1)[0].strip()

                new_filename = f"{show} - S{season}e{episode} - {episode_name}{file_extension}"
                os.rename(filename, new_filename)
                click.echo(f'Renamed:\n"{filename}"\nto:\n"{new_filename}"\n\n')

if __name__ == '__main__':
    rename_tv_series()
