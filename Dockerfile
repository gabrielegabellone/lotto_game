FROM python:3.9-alpine

# Create lotto_game directory
WORKDIR /lotto_game

# Copy all the modules in the image
COPY . /lotto_game

# When you execute the container the following command are executed
ENTRYPOINT ["python", "lotto_game.py"]