function confirmDeleteModal(id) {
  $('#deleteModal').modal();
  $('#deleteButton').html('<a href="/budget/delete/'+id+'" class="btn btn-danger" onclick="return closeDeleteModal('+id+')">Delete</a>');
}
function closeDeleteModal(id) {
  $('#deleteModal').modal('hide');
  return true
}
