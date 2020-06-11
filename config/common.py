REST_FRAMEWORK = {
    # 设置 DEFAULT_PAGINATION_CLASS 后，将全局启用分页，所有 List 接口的返回结果都会被分页。
    # 如果想单独控制每个接口的分页情况，可不设置这个选项，而是在视图函数中进行配置
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # 这个选项控制分页后每页的资源个数
    "PAGE_SIZE": 10,
}