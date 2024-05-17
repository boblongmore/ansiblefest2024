#!/usr/bin/python

# Copyright: (c) 2024, Bob Longmore <bob.longmore@wwt.com>
# GNU General Public License v3.0+ (see COPYING or
# https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: kafka_producer

short_description: Module to produce topics and information to kafka

version_added: "1.0.1"

description:

options:
    host:
        description: The host where kafka topic is posted
        required: true
        type: str
    port:
        description: The port where the kafka host is listening
        required: true
        type: int
    verify_mode: check SSL from kafka host
    topic: the kafka topoic
    group_id: the kafka group id

# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Bob Longmore (@boblongmore)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  wwt.kafka.kafka_producer:
    host: kafka_server
    port: 9092
    topic: kafka_topic
    data: {
        "key": "value"
    }
'''

RETURN = r'''
# These are examples of possible return values, and in general should use
# other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule
import json
import asyncio
from aiokafka import AIOKafkaProducer


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        host=dict(type='str', required=True),
        port=dict(type='int', required=True),
        verify_mode=dict(type='bool', required=False, default=True),
        topic=dict(type='str', required=True),
        group_id=dict(type='str', required=False),
        data=dict(type='dict', required=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # produce kafka message
    host = module.params['host']
    port = module.params['port']
    topic = module.params['topic']
    data = module.params['data']
    group_id = module.params['group_id']
    verify_mode = module.params['verify_mode']

    def serializer(value):
        return json.dumps(value).encode()

    async def produce():
        producer = AIOKafkaProducer(
            bootstrap_servers=f'{host}:{port}',
            value_serializer=serializer,
            compression_type="gzip")

        await producer.start()
        k_data = data
        await producer.send(topic, k_data)
        await producer.stop()

    asyncio.run(produce())

    # producer = KafkaProducer(bootstrap_servers=[f'{host}:{port}'])
#
    # producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
    # producer.send(topic, {data})

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    # result['original_message'] = module.params['name']
    # result['message'] = 'goodbye'

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    # if module.params['new']:
    #     result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    # if module.params['name'] == 'fail me':
    #     module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
