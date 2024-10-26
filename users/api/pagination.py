from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = "pageSize"
    page_query_param = "pageNumber"

    def get_paginated_response(self, data):
        return Response(
            {
                "pageNumber": self.page.number,
                "pageSize": self.page.paginator.per_page,
                "totalCount": self.page.paginator.count,
                "users": data,
            }
        )
