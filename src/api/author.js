import request from '@/utils/request'

export function createAuthorInfo(data) {
  return request({
    url: "/author/",
    method: 'post',
    data
  })
}

export function getAuthorInfo() {
  return request({
    url: "/author/",
    method: 'get',
  })
}

export function getAuthorInfoById(id) {
  return request({
    url: "/author/" + id,
    method: 'get',
  })
}

export function UpdateAuthorInfoById(id) {
  return request({
    url: "/author/" + id,
    method: 'put',
  })
}

export function DeleteAuthorInfoById(id) {
  return request({
    url: "/author/" + id,
    method: 'delete',
  })
}
