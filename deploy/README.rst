========================
Tamales Ansible Playbook
========================

You need to have root access into a remote server via SSH with a public key.

Install `ansible <http://docs.ansible.com/ansible/intro_installation.html>`_ and run::

    cd deploy
    cp hosts.example hosts
    vim hosts # add your remote server
    ansible-playbook -i hosts site.yml
