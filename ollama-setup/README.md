
# Running Models Locally using Ollama

## References:
1. [Ollama Docker Registry](https://hub.docker.com/r/ollama/ollama)

## What is Ollama ?
Ollama is a free, open-source platform that lets you download and run large language models (LLMs) directly on your own computer.

## Intalling Ollama using Docker

**CPU Only Setup:**

1. Running the container. This will also automatically pull the image from Docker Hub if not exists.

    ```sh
    docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama -e OLLAMA_CONTEXT_LENGTH=2048 ollama/ollama
    ```
    The option `-e` sets the specified environment variable within the container. Omit it if you would want more context length.

**GPU Setup:**

1. Check that your NVIDIA GPU and driver are working
   
    ```sh
    nvidia-smi
    ```
    You should see your GeForce GTX model, the installed NVIDIA driver version, and GPU memory information.
    If it fails, check your installed graphics driver:
    ```sh
    inxi -G
    mhwd -li # for Manjaro Linux
    ```

2. Install NVIDIA Container Toolkit

    The NVIDIA Container Tools makes your computer's GPU accessible to Docker containers. First, check whether the toolkit is available in your configured repositories

    ```sh
    pacman -Ss nvidia-container-toolkit
    ```

    Install it if available

    ```sh
    sudo pacman -S nvidia-container-toolkit
    ```

3. Configure Docker to use the NVIDIA driver

    Once the toolkit is installed, run the same Docker configuration commands recommended by Ollama and NVIDIA:

    ```sh
    sudo nvidia-ctk runtime configure --runtime=docker
    sudo systemctl restart docker
    ```

    * The first command configures Docker's daemon settings so that it can use NVIDIA's container runtime. It updates the file `/etc/docker/daemon.json`
    * The second restarts Docker to apply the changes.

4. Test GPU access from Docker

    Before running Ollama, verify that a container can actually see your GPU:

    ```sh
    docker run --rm --gpus=all \
        nvidia/cuda:12.1.1-runtime-ubuntu22.04 \
        nvidia-smi
    ```

    This uses a CUDA container to test GPU access independently of Ollama. The command is based on the GPU-testing approach documented by Arch Linux. The output inside the container should show your GeForce GTX GPU and driver information.
    
     Here's what each of the option does:

    | Option / Argument                        | Purpose                                                                                                                |
    | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
    | `docker run`                             | Creates and starts a new Docker container.                                                                             |
    | `--rm`                                   | Automatically removes the container after it exits.                                                                    |
    | `--gpus=all`                             | Exposes all available NVIDIA GPUs to the container.                                                                    |
    | `nvidia/cuda:12.1.1-runtime-ubuntu22.04` | Specifies the Docker image to use: NVIDIA CUDA 12.1.1 runtime based on Ubuntu 22.04.                                   |
    | `nvidia-smi`                             | Runs the NVIDIA System Management Interface utility inside the container to display GPU information and driver status. |

5. Run Ollama with GPU access

    ```sh
    docker run -d \
        --gpus=all \
        -v ollama:/root/.ollama \
        -p 11434:11434 \
        --name ollama \
        ollama/ollama
    ```


    Here's what each option does:
    
    | Option                    | Purpose                                             |
    | ------------------------- | --------------------------------------------------- |
    | `-d`                      | Runs the container in the background.               |
    | `--gpus=all`              | Exposes all available NVIDIA GPUs to the container. |
    | `-v ollama:/root/.ollama` | Persists downloaded models in a Docker volume.      |
    | `-p 11434:11434`          | Exposes Ollama's API on port 11434.                 |
    | `--name ollama`           | Names the container `ollama`.                       |
    | `ollama/ollama`           | Uses the official Ollama image.                     |



## Running Ollama(Using Docker)


1. Downloading an AI Model within the docker container.
 
    ```sh
    # syntax
    docker exec -it <container_name_or_id> ollama pull <model_name>

    # example
    docker exec -it ollama ollama pull gemma:2b
    ```

2. Verify the installation
    ```sh
    docker exec -it ollama ollama list
    ```

    You can also get a list of models by making an HTTP GET Request to the Ollama API that's running within the container:

    ```sh
    curl http://localhost:11434/api/tags
    ```
    You should get a JSON response listing the models available to Ollama.

3. Prompt the AI Model
    ```sh
    # syntax
    docker exec -it ollama ollama run <model-name> "Your Prompt Here"

    # example
    docker exec -it ollama ollama run gemma:2b "What is 2 + 3 ?"
    ```

    * The above command will download the model if it does not exist already, hence the first run can take time.
    * Use `docker stats` to monitor the memory usage while the AI model runs in your machine within the docker container.


## Installing Open Web UI (Docker Setup)

Open web UI starts Web App with a User Interface to chat with the AI model.

1. Running the Container:

    ```bash
    docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data -e WEBUI_SECRET_KEY=<your-secret-key> --name open-webui --restart always ghcr.io/open-webui/open-webui:main
    ```

    Remember the secret key you've generated since you may require it for future use.

## Trouble Shooting:

While Trying to chat with and AI model within the Open Web UI App, you may encounter the following errors:

1. > registry.ollama.ai/library/gemma:2b does not support tools

    Open WebUI is sending a tools payload along with your chat request. This happens when you have Native function calling enabled for the model, or a tool, web search, or code interpreter toggled on. But the model in use has no tool-calling support in its template, so Ollama rejects the request.

    To resolve this follow these steps:
    1. Click on your profile
    2. Click on Admin Panel
    3. Click on Settings option from the Breadcrumb
    4. In the settings page select "Model", you should see a list of installed models
    5. Click on Edit model
    6. Check the **Tools** or **Builtin Tools**, then disable all tools.

2. > llama-server process has terminated: signal: killed

    “Killed” (SIGKILL) almost always means the out-of-memory killer stopped the model process.

    1. Raise Docker’s memory limit. In Docker Desktop, go to Settings → Resources and set memory to at least 6 to 8 GB. On Windows/WSL2, set memory=8GB in `%UserProfile%\.wslconfig and run wsl --shutdown`.

    2. Reduce the context size. Add this to your Ollama container’s environment (`docker run -e` or compose `environment:`): `OLLAMA_CONTEXT_LENGTH=2048`.

