<template>
  <div class="app-container">
    <!-- 添加作者信息按钮 -->
    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button type="primary" icon="el-icon-plus" size="mini" @click="handleAdd">新增</el-button>
      </el-col>
    </el-row>
    <!--作者信息列表 -->
    <el-table :data="tableData" border style="width: 100%">
      <el-table-column prop="id" label="序号" width="180"></el-table-column>
      <el-table-column prop="first_name" label="姓名"></el-table-column>
      <el-table-column prop="last_name" label="笔名"></el-table-column>
      <el-table-column label="操作" width="180" align="center">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <!--添加作者信息表单-->
    <el-dialog :title="title" :visible.sync="centerDialogVisible" width="50%" center>
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="作者姓名">
          <el-input v-model="form.first_name"></el-input>
        </el-form-item>
        <el-form-item label="作者笔名">
          <el-input v-model="form.last_name"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancel">取 消</el-button>
        <el-button type="primary" @click="save">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import {
  createAuthorInfo,
  getAuthorInfo,
  getAuthorInfoById,
  UpdateAuthorInfoById,
  DeleteAuthorInfoById
} from "@/api/author";
export default {
  data() {
    return {
      tableData: [],
      centerDialogVisible: false,
      form: {
        first_name: "",
        last_name: ""
      },
      title: "添加作者信息"
    };
  },
  methods: {
    handleAdd() {
      this.centerDialogVisible = true;
      this.title = "添加作者信息";
    },
    handleCreate() {
      createAuthorInfo({
        first_name: this.form.first_name,
        last_name: this.form.last_name
      })
        .then(res => {
          if (res.code === "success") {
            this.$message.success("添加成功");
            this.getAuthorList();
          } else {
            this.$message.error("添加失败");
          }
        })
        .catch(err => {
          this.$message.error("服务端异常，添加失败。");
        });
    },
    handleUpdate() {
      UpdateAuthorInfoById(this.form)
        .then(res => {
          if (res.code === "success") {
            this.$message.success("更新成功");
          } else {
            this.$message.error("更新失败");
          }
        })
        .catch(err => {
          this.$message.error("服务端异常，更新失败。");
        });
    },
    handleDelete(index, row) {
      const auhtorId = row.id;
      DeleteAuthorInfoById(auhtorId)
        .then(res => {
          if (res.code === "success") {
            this.$message.success("删除成功");
            this.getAuthorList();
          } else {
            this.$message.error("删除失败");
          }
        })
        .catch(err => {
          this.$message.error("删除失败");
        });
    },
    handleEdit(index, row) {
      this.centerDialogVisible = true;
      this.title = "编辑作者信息";
      this.form = row;
    },
    getAuthorList() {
      getAuthorInfo()
        .then(res => {
          if (res.code === "success") {
            this.tableData = res.authors;
          } else {
            this.$message.error("获取信息失败");
          }
        })
        .catch(err => {
          this.$message.error("服务端异常，请联系管理员解决。");
        });
    },
    save() {
      if (this.title === "添加作者信息") {
        this.handleCreate();
      } else {
        this.handleUpdate();
      }
      this.centerDialogVisible = false;
    },
    cancel() {
      this.centerDialogVisible = false;
      this.reset();
    },
    reset() {
      this.form = {
        first_name: "",
        last_name: ""
      };
    }
  },
  mounted() {
    this.getAuthorList();
  }
};
</script>

<style lang="css">
.mb8 {
  margin-bottom: 8px;
}
</style>
