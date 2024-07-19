# Automated Software Image Management Ansiblefest2024


![Platform Pete](images/platform_pete.png)

This repo was developed to showcase Ansible Automation Platform and Event-Driven Ansible for Red Hat Summit 2024.

## Presentation Abstract

Software Image Management (SWIM) is a repeatable framework in which engineers can produce repeatable, safe outcomes for efficient software upgrades for devices. This produces faster response to vulnerability management, more predictable maintenance schedules, and hours of an engineer’s life saved in the middle of the night.

**Reusability:** Building functions in small roles or playbooks allow for use of that function in many different scenarios (testing)

**Consumability:** Building a common workflow to upgrade devices in a multi-OEM environment

**Improvement:** Testing, Testing, Testing. Not only of device functionality, but of service health pre- and post-upgrade. This allows for peace of mind that an update has not introduced system-wide issues. Automation engineers can iterate further tasks such as documentation, ticketing, clearing alerts, etc.

Get back to bed sooner!


## Technologies Used

- Ansible Automation Platform
- Event-Driven Ansible
- Arista Networks
- [Netbox](https://github.com/netbox-community/netbox-docker)
- [Kafka](https://hub.docker.com/r/landoop/fast-data-dev)
- Slack

## Other Ansible Projects Referenced

The Arista tests used in this presentation are located here: [github.com/boblongmore/arista_network_tests](https://github.com/boblongmore/arista_network_tests)

The kafka producer module is available as part of the [wwt.kafka](https://galaxy.ansible.com/ui/repo/published/wwt/kafka/) collection in galaxy.

## Tenets of SWIM

Automated testing that is extensible and modular helps improve reliability of SWIM.

pre-, upgrade, post-

## Why use EDA and Kafka

integrations, modularity

Bob Longmore bob.longmore@wwt.com
