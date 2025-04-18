Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-22.04"

  # Global synced folder (application files available)
  config.vm.synced_folder ".", "/vagrant"

  SWARM_MASTER_IP = "192.168.33.10"

  # Master Node (masteryc)
  config.vm.define "masteryc" do |masteryc|
    masteryc.vm.hostname = "masteryc"
    masteryc.vm.network "private_network", ip: SWARM_MASTER_IP
    masteryc.vm.network "forwarded_port", guest: 80, host: 8080

    masteryc.vm.provider "virtualbox" do |vb|
      vb.name = "masteryc"
      vb.memory = "4096"
      vb.cpus = 2
    end

    masteryc.vm.provision "shell", inline: <<-SHELL
      curl -fsSL https://get.docker.com | sh
      sudo usermod -aG docker vagrant
      
      # Install Java for Jenkins (optional)
      sudo apt-get update -y
      sudo apt-get install -y openjdk-17-jdk

      # Initialize Docker Swarm on Master
      sudo docker swarm init --advertise-addr #{SWARM_MASTER_IP}

      # Save Worker Join Command for easy access
      sudo docker swarm join-token worker -q > /vagrant/worker_token
    SHELL
  end

  # Worker Node (nodoyc)
  config.vm.define "nodoyc" do |nodoyc|
    nodoyc.vm.hostname = "nodoyc"
    nodoyc.vm.network "private_network", ip: "192.168.33.11"

    nodoyc.vm.provider "virtualbox" do |vb|
      vb.name = "nodoyc"
      vb.memory = "2048"
      vb.cpus = 1
    end

    nodoyc.vm.provision "shell", inline: <<-SHELL
      curl -fsSL https://get.docker.com | sh
      sudo usermod -aG docker vagrant

      sudo apt-get update -y
      sudo apt-get install -y python3

      # Wait for the Master token to become available
      while [ ! -f /vagrant/worker_token ]; do sleep 2; done

      # Retrieve token and join swarm
      SWARM_TOKEN=$(cat /vagrant/worker_token)
      sudo docker swarm join --token $SWARM_TOKEN #{SWARM_MASTER_IP}:2377
    SHELL
  end
end