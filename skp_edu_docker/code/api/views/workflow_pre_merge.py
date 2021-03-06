import json
from rest_framework.response import Response
from rest_framework.views import APIView
from master.workflow.preprocess.workflow_pre_merge import WorkFlowPreMerge as WFPreMerge
import coreapi

class WorkFlowPreMerge(APIView) :
    # TODO:add document sample for swagger (need to update)
    coreapi_fields = (
        coreapi.Field(
            name='parm1',
            required=True,
            type='string',
        ),
        coreapi.Field(
            name='parm2',
            required=True,
            type='string',
        ),
    )
    def post(self, request, nnid, ver, node, type):
        """
        - desc : insert data
        """
        try:
            input_data = request.data
            nodeid = ''.join([nnid, '_', ver, '_', node])
            input_data['type'] = type
            if (WFPreMerge().validation_check(input_data)):
                return_data = WFPreMerge().set_view_obj(nodeid, input_data)
            else :
                return_data = {'message' : 'data validation error'}
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def get(self, request, nnid, ver, node, type):
        """
        - desc : get data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def put(self, request, nnid, ver, node, type):
        """
        - desc ; update data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def delete(self, request, nnid, ver, node, type):
        """
        - desc : delete  data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))
